public class Main {
    abstract class ArmaStrategy {
        public abstract void arma();
        
    }
    
     class Caracter {
        public  void pelear();
        public  ArmaStrategy getArma();
        public  void setArma(ArmaStrategy arma);
    }

    class Espada extends ArmaStrategy {
        @Override
        public void arma() {
            System.out.println("Usando espada");
        }
    }

    class Arco extends ArmaStrategy {
        @Override
        public void arma() {
            System.out.println("Usando arco");
        }
    }

    class Cuchillo extends ArmaStrategy {
        @Override
        public void arma() {
            System.out.println("Usando cuchillo");
        }
    }

    class Hacha extends ArmaStrategy {
        @Override
        public void arma() {
            System.out.println("Usando hacha");
        }
    }

    class testCaracter{
        public testCaracter() {
            Caracter guerrero = new Caracter() {
                private ArmaStrategy arma;

                @Override
                public void pelear() {
                    System.out.println("Guerrero peleando");
                    if (arma != null) {
                        arma.arma();
                    } else {
                        System.out.println("No tiene arma asignada");
                    }
                }

                @Override
                public ArmaStrategy getArma() {
                    return arma;
                }

                @Override
                public void setArma(ArmaStrategy arma) {
                    this.arma = arma;
                }
            };

            guerrero.setArma(new Espada());
            guerrero.pelear();

            guerrero.setArma(new Hacha());
            guerrero.pelear();
        }

        public static void main(String[] args) {
            new testCaracter();
        }
    }
}
