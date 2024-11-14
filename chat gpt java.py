import java.util.ArrayList;
import java.util.Scanner;

// Classe abstrata Moeda
abstract class Moeda {
    protected double valor;

    public Moeda(double valor) {
        this.valor = valor;
    }

    public double getValor() {
        return valor;
    }

    public abstract String getNome();
}

// Classe Dolar
class Dolar extends Moeda {
    public Dolar(double valor) {
        super(valor);
    }

    @Override
    public String getNome() {
        return "Dólar";
    }
}

// Classe Euro
class Euro extends Moeda {
    public Euro(double valor) {
        super(valor);
    }

    @Override
    public String getNome() {
        return "Euro";
    }
}

// Classe Real
class Real extends Moeda {
    public Real(double valor) {
        super(valor);
    }

    @Override
    public String getNome() {
        return "Real";
    }
}

// Classe Cofrinho
class Cofrinho {
    private ArrayList<Moeda> moedas;

    public Cofrinho() {
        moedas = new ArrayList<>();
    }

    public void adicionarMoeda(Moeda moeda) {
        moedas.add(moeda);
    }

    public void removerMoeda(int indice) {
        moedas.remove(indice);
    }

    public void listarMoedas() {
        System.out.println("Moedas no cofrinho:");
        for (int i = 0; i < moedas.size(); i++) {
            Moeda moeda = moedas.get(i);
            System.out.println(i + 1 + ". " + moeda.getNome() + ": " + moeda.getValor());
        }
    }

    public double calcularTotal() {
        double total = 0;
        for (Moeda moeda : moedas) {
            total += moeda.getValor();
        }
        return total;
    }
}

public class Principal {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Cofrinho cofrinho = new Cofrinho();

        while (true) {
            System.out.println("Escolha uma opção:");
            System.out.println("1. Adicionar moeda");
            System.out.println("2. Remover moeda");
            System.out.println("3. Listar moedas");
            System.out.println("4. Calcular total");
            System.out.println("5. Sair");

            int opcao = scanner.nextInt();
            scanner.nextLine(); // Limpar o buffer

            switch (opcao) {
                case 1:
                    System.out.println("Digite o valor da moeda:");
                    double valor = scanner.nextDouble();
                    scanner.nextLine(); // Limpar o buffer
                    System.out.println("Digite o tipo da moeda (Dolar, Euro, Real, etc.):");
                    String tipo = scanner.nextLine();
                    switch (tipo.toLowerCase()) {
                        case "dolar":
                            cofrinho.adicionarMoeda(new Dolar(valor));
                            break;
                        case "euro":
                            cofrinho.adicionarMoeda(new Euro(valor));
                            break;
                        case "real":
                            cofrinho.adicionarMoeda(new Real(valor));
                            break;
                        default:
                            System.out.println("Tipo de moeda inválido.");
                    }
                    break;
                case 2:
                    System.out.println("Digite o índice da moeda a ser removida:");
                    int indice = scanner.nextInt();
                    cofrinho.removerMoeda(indice - 1);
                    break;
                case 3:
                    cofrinho.listarMoedas();
                    break;
                case 4:
                    System.out.println("Total no cofrinho: R$" + cofrinho.calcularTotal());
                    break;
                case 5:
                    System.out.println("Saindo...");
                    System.exit(0);
                    break;
                default:
                    System.out.println("Opção inválida.");
            }
        }
    }
}