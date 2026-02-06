public class Main{
 
    abstract class Figure {
        public abstract double getPerimeter();
        public abstract double getArea();

    }

    class Triangle extends Figure {
        private double sideA;
        private double sideB;
        private double sideC;

        public Triangle(double sideA, double sideB, double sideC) {
            this.sideA = sideA;
            this.sideB = sideB;
            this.sideC = sideC;
        }

        @Override
        public double getPerimeter() {
            if(this.sideA <= 0 || this.sideB <= 0 || this.sideC <= 0) {
                System.out.println("Error: Triangle sides must be positive.");
                return 0;
            }
            else if (this.sideA < this.sideB + this.sideC &&
                     this.sideB < this.sideA + this.sideC &&
                     this.sideC < this.sideA + this.sideB) {
                return sideA + sideB + sideC;
            } else {
                System.out.println("Error: The provided sides do not form a valid triangle.");
                return 0;            
            }
        }

        @Override
        public double getArea() {
            if(this.sideA <= 0 || this.sideB <= 0 || this.sideC <= 0) {
                System.out.println("Error: Triangle sides must be positive.");
                return 0;
            }
            else if (this.sideA < this.sideB + this.sideC &&
                     this.sideB < this.sideA + this.sideC &&
                     this.sideC < this.sideA + this.sideB) {
                double s = getPerimeter() / 2;
                return Math.sqrt(s * (s - sideA) * (s - sideB) * (s - sideC));
            } else {
                System.out.println("Error: The provided sides do not form a valid triangle.");
            }
            return 0;
        }
    
    }

    class Rectangle extends Figure {
        private double length;
        private double width;

        public Rectangle(double length, double width) {
            this.length = length;
            this.width = width;
        }

        @Override
        public double getPerimeter() {
            if(this.length <= 0 || this.width <= 0) {
                System.out.println("Error: Rectangle sides must be positive.");
                return 0;
            }
            return 2 * (length + width);
        }

        @Override
        public double getArea() {
            if(this.length <= 0 || this.width <= 0) {
                System.out.println("Error: Rectangle sides must be positive.");
                return 0;
            }
            return length * width;
        }
    }

    class Circle extends Figure {
        private double radius;

        public Circle(double radius) {
            this.radius = radius;
        }

        @Override
        public double getPerimeter() {
            if(this.radius <= 0) {
                System.out.println("Error: Circle radius must be positive.");
                return 0;
            }
            return 2 * Math.PI * radius;
        }

        @Override
        public double getArea() {
            if(this.radius <= 0) {
                System.out.println("Error: Circle radius must be positive.");
                return 0;
            }
            return Math.PI * radius * radius;
        }
    }

    class testTriangle {
        public testTriangle() {
            System.out.println("==========================TRIANGLE CLASS TESTS==========================\n");
            System.out.println("Testing Triangle class with various inputs:\n");
            Triangle trianglePositiveNumbers = new Triangle(3, 4, 5);
            Triangle triangleNegativeNumbers = new Triangle(-3, -4, -5);
            Triangle triangleZero = new Triangle(0, 0, 0);
            Triangle triangleImpossible = new Triangle(1,1, 100);

            Triangle[] listOfTriangles = {trianglePositiveNumbers, triangleNegativeNumbers, triangleZero, triangleImpossible};
            
            int triangleCount = 1;
            for (Triangle triangle : listOfTriangles) {
                System.out.println("---- Triangle " + triangleCount + " ----");
                System.out.println(">> Sides: " + triangle.sideA + ", " + triangle.sideB + ", " + triangle.sideC);
                System.out.println(">> Perimeter: " + triangle.getPerimeter());
                System.out.println(">> Area: " + triangle.getArea() + "\n");
                triangleCount++;
            }
        }
    }

    class testRectangle {
        public testRectangle() {
            System.out.println("==========================RECTANGLE CLASS TESTS==========================\n");
            System.out.println("Testing Rectangle class with various inputs:\n");
            Rectangle rectanglePositiveNumbers = new Rectangle(4, 5);
            Rectangle rectangleNegativeNumbers = new Rectangle(-4, -5);
            Rectangle rectangleZero = new Rectangle(0, 0);

            Rectangle[] listOfRectangles = {rectanglePositiveNumbers, rectangleNegativeNumbers, rectangleZero};
            
            int rectangleCount = 1;
            for (Rectangle rectangle : listOfRectangles) {
                System.out.println("---- Rectangle " + rectangleCount + " ----");
                System.out.println(">> Sides: " + rectangle.length + ", " + rectangle.width);
                System.out.println(">> Perimeter: " + rectangle.getPerimeter());
                System.out.println(">> Area: " + rectangle.getArea() + "\n");
                rectangleCount++;
            }
        }
    }

    class testCircle {
        public testCircle() {
            System.out.println("==========================CIRCLE CLASS TESTS==========================\n");
            System.out.println("Testing Circle class with various inputs:\n");
            Circle circlePositiveNumber = new Circle(5);
            Circle circleNegativeNumber = new Circle(-5);
            Circle circleZero = new Circle(0);

            Circle[] listOfCircles = {circlePositiveNumber, circleNegativeNumber, circleZero};
            
            int circleCount = 1;
            for (Circle circle : listOfCircles) {
                System.out.println("---- Circle " + circleCount + " ----");
                System.out.println(">> Radius: " + circle.radius);
                System.out.println(">> Perimeter: " + circle.getPerimeter());
                System.out.println(">> Area: " + circle.getArea() + "\n");
                circleCount++;
            }
        }
    }

    public static void main(String[] args) {
        Main main = new Main();
        testTriangle test = main.new testTriangle();
        testRectangle test2 = main.new testRectangle();
        testCircle test3 = main.new testCircle();
    }
}