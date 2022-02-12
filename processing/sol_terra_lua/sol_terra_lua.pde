float n;
float r;

void setup ()
{
  fullScreen();
}

void draw ()
{
  background(20);
  translate(width/2, height/2);
  stroke(#ffff85);
  fill(#ffff85);
  circle(0,0,200);
  rotate(frameCount/(20*TWO_PI));
  stroke(#2bab42);
  fill(#2bab42);
  circle(width/4,0,100);
  
  pushMatrix();
  translate(width/4, 0);
  rotate(frameCount/(10*TWO_PI));
  stroke(#9e9e9e);
  fill(#9e9e9e);
  circle(80,0,20);
  popMatrix();
}
