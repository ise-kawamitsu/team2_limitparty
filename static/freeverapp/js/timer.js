var to_timeup = 900; //set time
var max = 900; //reset time
var intervalid;
var start_flag = false;

function count_start(){
    if(start_flag===false){                          
        intervalid = setInterval(count_down,1000);  
        start_flag = true;
    }
}

function count_down(){
    let timer = document.getElementById("timer");  
    if(to_timeup===0){
        timer.innerHTML = 'Time up!'
        timer.style.color="red"; 
        alert('Time up!')
        count_stop();
    }   else {
        to_timeup--;
        padding();
    }
}

function padding(){
    let timer=document.getElementById("timer");   
    let min = 0;
    let sec = 0;
    min = Math.floor(to_timeup/60);
    sec = (to_timeup%60);
    min = ("0"+min).slice(-2);
    sec = ("0"+sec).slice(-2);
    timer.innerHTML = min +":"+ sec;
}

function count_stop(){
    console.log(count_stop);
    clearInterval(intervalid);
    start_flag = false;
}

function count_reset(){
    console.log(count_reset);
    let timer = document.getElementById("timer");
    clearInterval(intervalid);
    start_flag = false;
    to_timeup = max; 
    padding();
    timer.style.color = "black";   
}

window.onload = function(){
    padding();
    let startbutton=document.getElementById("startbutton");
    startbutton.addEventListener("click",count_start,false);
    let stopbutton=document.getElementById("stopbutton");
    stopbutton.addEventListener("click",count_stop,false);
    let resetbutton=document.getElementById("resetbutton");
    resetbutton.addEventListener("click",count_reset,false);
}  