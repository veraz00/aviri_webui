$(document).ready(function(){
    $('.image').click(function(){
         $(this).css('width', function(_ , cur){
          return cur === '100px' ? '100%' : '100px'
        });  // original width is 500px 
    });
});