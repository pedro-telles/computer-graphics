class Ponto {
  float x, y;
  
  Ponto (float x, float y) {
    this.x = x;
    this.y = y;
  }
  
  void draw_point() {
    circle(x, y, 5);
  }
}

void setup() {
  fullScreen();
  noFill();
  stroke(255);
}

void draw() {
  background(0);
  translate(width/2, height/2);
  
  Ponto p1 = null, p2 = null, p3 = null, p4 = null;

  p1 = new Ponto(-500, 0);
  p2 = new Ponto(500, 0);
  p3 = new Ponto(-250, 250);
  p4 = new Ponto(250, -250);

  beginShape();
  
  fill(255);
  p1.draw_point();
  p2.draw_point();
  
  for(float t = 0; t <= 1; t += 0.01)
  {
    Ponto pa = find_point(p1, p3, t);
    Ponto pb = find_point(p3, p4, t);
    Ponto pc = find_point(p4, p2, t);
    Ponto pd = find_point(pa, pb, t);
    Ponto pe = find_point(pb, pc, t);
    Ponto pf = find_point(pd, pe, t);
    
    noFill();
    vertex(pf.x,pf.y);  
  }
  
  endShape();
}

Ponto find_point(Ponto p1, Ponto p2, float t) {
  float x = p1.x + t*(p2.x - p1.x);
  float y = p1.y + t*(p2.y - p1.y);
  
  Ponto pr = new Ponto(x, y);
  
  return pr;
}
