float n = 0;
float r = 0;
float aNext = 0;
float rProx = 0;

void setup ()
{
  size(1920,1080);
  background(20);
  stroke(255);
}

public void draw () 
{
  translate(width/2, height/2);
  line(cos(n) * r, sin(n) * r, cos(aNext) * rProx, sin(aNext) * rProx);
  n = aNext;
  r = rProx;
  aNext = aNext + 0.05;
  rProx = rProx + 0.1;
}
