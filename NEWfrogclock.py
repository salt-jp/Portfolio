let sec;
let min;
let hr;
let mill;

let x = 10;
let speed = 2;

//blink check
let check = 30;
function setup() {
	createCanvas(windowWidth, windowHeight);
	background(0,50,100);
}

function draw() {
	fill(0,100,50);
	ellipse(510 + 400, 850, 700, 200);	
	
	
fill(1, 255, 100);
  noStroke();
	//head
  ellipse(510 + 400, 450, 600 - 175, 500-175);
  ellipse(370 + 390, 300, 300 - 175, 300-175);
  ellipse(670 + 390, 300, 300 - 175, 300-175);
	ellipse(510 + 400, 700, 700 - 175, 600-175);
  
	//feet
	arc(760, 875, 280, 180, PI, PI + HALF_PI);
	arc(1060, 875, 280, 180, PI + HALF_PI, TWO_PI);
	
	//stomach
	fill('Yellow')
	ellipse(510 + 400, 725, 700 - 250, 600-250);
	
	//white eyes
  fill(255);
  ellipse(370 + 390, 300, 200 - 100, 200-100);
  ellipse(670 + 390, 300, 200 - 100, 200-100);
	
	//fill(0);
		//rect(655 + 370, 300, 80, 20);
		//rect(655 + 70, 300, 80, 20);
  
	//pupils
  fill(0);
	if(sec % 2 != 0) {
		//if seconds is odd eyes are on the left
		ellipse(355 + 390, 300, 100-45, 100-45);
  ellipse(655 + 390, 300, 100-45, 100-45);
	}
  
	if(sec % 2 == 0) {
		//if seconds are even eyes are on the right
		ellipse(385 + 390, 300, 100-45, 100-45);
		ellipse(685+390, 300, 100-45, 100-45);
	}
	
		//blink
	if(min == check) {
		//green color
		fill(1, 255, 100);
		
		//white eyes
		ellipse(370 + 390, 300, 200 - 100, 200 - 100);
		ellipse(670 +390, 300, 200 - 100, 200 - 100);
		//if seconds are even eyes are on the right
		ellipse(375 + 390, 300, 100-45, 100-45);
		ellipse(675+390, 300, 100-45, 100-45);
		//if seconds is odd eyes are on the left
	ellipse(370 + 390, 300, 100-45, 100-45);
  ellipse(670 + 390, 300, 100-45, 100-45);
		
	//rectangle trying shit
			
		fill(0);
			rect(655 + 370, 300, 80, 10);
		rect(655 + 70, 300, 80, 10);
	
		

	}
	
	//question
	fill(0);
  
	//nostrils
  ellipse(480 + 400, 470, 20, 20);
  ellipse(540 + 400, 470, 20, 20);

	
	
	
		
	sec = second();
	min = minute();
	hr = hour();
	
	

	{
		
		
	
		
		
	}
	//text
	fill(255, 153, 51);
	textSize(185);
	
	text(hr ,805, 775);
	
	{
		
		{
			fill(255, 153, 51);
			textSize(90);
			
			text(min, 860,850);
		}
		
	//}	
	
	//	 ellipse(x, height/2, 20, 20);
  //x = x + speed;
  
  //if(x > width - 10 || x < 10){
  //  speed = -speed;
	//}
	
	
	
	}}
