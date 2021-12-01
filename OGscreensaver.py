//took this from some class notes from Whalen 
let bouncers = [];


class Bouncer {
		constructor(x,y,vx,vy){
			this.x = x;
			this.y = y;
			this.vx = vx;
			this.vy = vy;
		}
	
		update(){
			this.x += this.vx;
			this.y += this.vy;
			
			
				if (this.x < (0 + 25) || this.x > (width - 25)){
						this.vx = -this.vx;
					}
					if (this.y < (0 + 25) || this.y > (height - 25)){
						this.vy = -this.vy;
					}
		}
	
	  show(){
			rect(this.x,this.y,50,30);
			//triangle(this.x,this.y, 50, 50); this makes weird line and its kinda cool so backup i guess 
		}
}
function setup() {
	createCanvas(windowWidth, windowHeight);
	
	
	setInterval(colorChange, 7000);
	for (var b = 0; b <= 200; b += 1){
		bouncers.push(new Bouncer(random(width),random(height),random(-2,2),random(-2,2)));	
	}
	
	
	
}

function draw() {
	background(5,10,10);
	for (var i = 0; i < 100; i += 1){ 
		for (var j = 0; j < 100; j += 1){ 
			rect(10 + (i * 30),5 + (j * 100),1); 


				
			
		}
	}
	//this is from a previous sketch I made, but it's from the moving and bouncing module I think
	//this is for the big rectangles
	
	//right rectangle 
		if (x < (0 + 1) || x > (width - 100)){
		vx = -vx;
	}
	if (y < (0 + 1) || y > (height - 100)){
		vy = -vy;
	}
	x += vx;
	y += vy;
	rect(1600,y, 100,1000);
	noStroke(); 
	
	
	
	//maybe new rect between right and mid
	//		if (x < (0 + 1) || x > (width - 100)){
	//	vx = -vx;
//}
	//if (y < (0 + 1) || y > (height - 100)){
	//	vy = -vy;
	//}
	//x += vx;
	//y += vy;
	//rect(1200,y, 100,1000);
	//noStroke(); 
	
	//middle rectangle 
	
		if (x < (0 + 1) || x > (width - 100)){
		vx = -vx;
	}
	if (y < (0 + 1) || y > (height - 100)){
vy = -vy;
	}
	x += vx;
	y += vy;
	rect(840,y, 100,1000);
	noStroke(); 
	
	
	//maybe new rect bewtejqf yeah 
	//	if (x < (0 + 1) || x > (width - 100)){
	//	vx = -vx;
	//}
	//if (y < (0 + 1) || y > (height - 100)){
	//	vy = -vy;
	//}
	//x += vx;
	//y += vy;
	//rect(500,y, 100,1000);
	//noStroke(); 
	
	
	
	//left rectangle 
					if (x < (0 + 1) || x > (width - 100)){
		vx = -vx;
	}
	if (y < (0 + 1) || y > (height - 100)){
		vy = -vy;
	}
	x += vx;
	y += vy;
	rect(100,y, 100,1000);
	noStroke(); 

	for (var b = 0; b < bouncers.length; b += 1){
		bouncers[b].update();
		bouncers[b].show();
	}
	

}

//got the color from a p5js color pallete. (I don't think its a pallete, but the colors aren't totally random anymore for a better aesthetic) 
function colorChange() {
	 fill(random(10, 255), random(20, 200), 100);
	
	
}



let x = 100;
let y = 105;
let vx = 8;
let vy = 1;

//so this does something cool but im going to try it on another sketch 
//function draw() {
		//	if (x < (0 + 60) || x > (width - 25)){
		//vx = -vx;
//	}
	//if (y < (0 + 25) || y > (height - 25)){
	//	vy = -vy;
	//}
	//x += vx;
//	y += vy;
///	rect(1600,y, 50,40);
//	noStroke(); }
