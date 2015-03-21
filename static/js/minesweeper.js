/*
Reference: tim5046 https://github.com/tim5046/projectOdin/tree/master/Javascript/Minesweeper*/

$(document).ready(function(){

  	numCols = 8;
    numRows = 8;
	setBoard(numRows, numCols);

	$('#cheat').on("click", function(event){
		cheat();
	});

	$('#restartGame').on("click", function(event){
		restartGame();
	});

	$('#verify').on("click", function(event){
		validate();
	});

    $(document).on('mousedown','.left td',function(event){
      if( event.button === 0 ) {
      	console.log("at the stage of onMousedown" + $(this).attr('id'));
        checkCell($(this).attr('id'));
      }
    });
});

function validate(){
	console.log("verify");
	for (i = 0; i < numCols*numRows; i++ ) {
		cell = $('.board').find('#'+i);
		if (cell.hasClass('blank') && !cell.hasClass('bomb')) {
			$('#result').text("FINISH PLS");
			return;
		}
	}
    if ($('#result').text().length == 0){
        $('#result').text("GOOD JOB");
    }
	
}

function restartGame() {
	location.reload();
}

function cheat(){
	console.log("cheating!");
	for (i = 0; i < numCols*numRows; i++ ) {
		cell = $('.board').find('#'+i);
		if (cell.hasClass('bomb')) {
			$(cell).addClass('bomb-revealed');
		}
	}
}

function setBoard(x,y) {
	$('.board').append('<tr id="start"></tr>');
        
    var start=$('.board').find("#start");
   
    //cells!
    var counter=1;
    for(var j=0;j<y;j++){
        start.parent().last().append('<tr class="left" id ="cell">');
        for( i=0; i<x;i++){
            var newCount=i+counter;
            start.parent().last().find(".left").last().append('<td class="cell blank" id='+newCount+'></td>');
        }
        counter+=y;
        start.parent().last().find(".left").last().append('<td id="right">');    
    }
    
    setBombs(x,y);
}

//x,y usually 8*8= 64, 10 bombs hidden.  
function setBombs(x,y){
	var numBombs = 10;
	(function setBomb() {
		$('.bomb').each(function() {
			$(this).removeClass('bomb');
		});
		var rand = 0;
		for (var i=1; i < numBombs+1; i++) {
			rand = Math.floor(Math.random() * (x*y)) +1;
			var cell = $('.board').find('#'+rand);
			console.log(rand);
			if (cell.hasClass('bomb')) {
				$('.board').find('#'+rand+1)
				//if already has bomb, find a new place
			} else {
				cell.addClass('bomb');
			}
			rand = 0;
		}
	})();
}


function checkCell(id){
    cell = $('.board').find('#'+id);
	console.log("at the stage of checkcell" + id);

    if (cell.hasClass('bomb')){
    	console.log("bomb is clicked");
        $('.bomb').each(function() {
        $(this).addClass('bomb-revealed');
        endGame();
        });
           
    } else if (cell.hasClass('blank')){
        var bombCount = 0;
        id=parseInt(id,10);
        var adjacent=[];

        if (id % numCols === 0){
            adjacent=[(id - 1 - numCols),(id - numCols),(id-1),(id-1+numCols),(id+numCols)];           
        } else if (((id-1) % numCols === 0) || id == 1){ 
            adjacent=[(id - numCols),((id+1)-numCols),(id+1),(id+numCols),(id+1+numCols)];            
        } else if (id < numCols){ 
           adjacent=[(id-1),(id+1),(id-1+numCols),(id+numCols),(id+1+numCols)];             
        } else if ((((numCols*numRows)-numCols) < id) && id < (numCols*numRows)) { 
           adjacent=[(id - 1 - numCols),(id - numCols),((id+1)-numCols),(id-1),(id+1)];             
        } else { 
           adjacent=[(id - 1 - numCols),(id - numCols),((id+1)-numCols),(id-1),(id+1),(id-1+numCols),(id+numCols),(id+1+numCols)]; 
        } 
        
        adjacent.forEach(function(entry){
            if($('.board').find('#'+entry).hasClass('bomb')){
             	console.log("while for each, found bomb in " + entry);
             	bombCount++; 
            }
        });
       
        if (bombCount === 0){ 
            $(cell).removeClass('blank');
            $(cell).text(''); 
            $(cell).addClass('clicked'); 
            
            adjacent.forEach(function(entry){
                checkCell(entry);             
            });      

        } else {
        	console.log("bomb count" + bombCount);
            $(cell).removeClass('blank');
            $(cell).text(bombCount); 
            $(cell).addClass('clicked');    
        }

    }
}


function endGame(){
    $('.cell').each(function(){
     $(this).removeClass('blank');   
    });
    $('#result').text("YOU LOST");
    
}

