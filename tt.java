public enum ComputerType {
    DESKTOP, LAPTOP;
}



public enum Manufacturer {
    APPLE, DELL, HP, MICROSOFT, LENOVO;
}




public interface ComputerFunctions {
    public void doWork(double minutes);
    public void playGames(double minutes);
}




public abstract class Computer implements ComputerFunctions {
    private Manufacturer manufacturer;
    private ComputerType type;
    private int cost;
    private int ramSize;

    public Computer(Manufacturer manufacturer, ComputerType type, int cost, int ramSize) {
        this.manufacturer = manufacturer;
        this.type = type;
        this.cost = cost;
        this.ramSize = ramSize;
    }

    public Manufacturer getManufacturer() {
        return manufacturer;
    }

    public ComputerType getType() {
        return type;
    }

    public int getCost() {
        return cost;
    }

    public int getRamSize() {
        return ramSize;
    }

    public abstract String toString();  // Will be implemented in child classes

    @Override
    public abstract void doWork(double minutes);

    @Override
    public abstract void playGames(double minutes);

    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (obj == null || getClass() != obj.getClass()) return false;

        Computer computer = (Computer) obj;
        return cost == computer.cost &&
                manufacturer == computer.manufacturer &&
                type == computer.type;
    }
}




public class Laptop extends Computer {
    private double batteryLevel = 100.0;

    public Laptop(Manufacturer manufacturer, int cost, int ramSize) {
        super(manufacturer, ComputerType.LAPTOP, cost, ramSize);
    }

    public double getBatteryLevel() {
        return batteryLevel;
    }

    @Override
    public void doWork(double minutes) {
        batteryLevel -= minutes * 0.2;
    }

    @Override
    public void playGames(double minutes) {
        batteryLevel -= minutes * 0.3;
    }

    @Override
    public String toString() {
        return "Manufacturer:" + getManufacturer() + ", Type:" + getType() + ", Cost:" + getCost() + 
               ", RAM:" + getRamSize() + ", Battery:" + batteryLevel;
    }
}




public class Desktop extends Computer {
    private double hddLevel = 0.0;

    public Desktop(Manufacturer manufacturer, int cost, int ramSize) {
        super(manufacturer, ComputerType.DESKTOP, cost, ramSize);
    }

    public double getHddLevel() {
        return hddLevel;
    }

    @Override
    public void doWork(double minutes) {
        hddLevel += minutes * 1.5;
    }

    @Override
    public void playGames(double minutes) {
        hddLevel += minutes * 0.5;
    }

    @Override
    public String toString() {
        return "Manufacturer:" + getManufacturer() + ", Type:" + getType() + ", Cost:" + getCost() + 
               ", RAM:" + getRamSize() + ", HDDLevel:" + hddLevel;
    }
}




import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class ComputerTest {

    @Test
    public void testLaptopBatteryLevel() {
        Laptop laptop = new Laptop(Manufacturer.APPLE, 3500, 16);
        laptop.doWork(20);  // 20 minutes of work
        laptop.playGames(40);  // 40 minutes of games
        assertEquals(84.0, laptop.getBatteryLevel());
    }

    @Test
    public void testDesktopHddLevel() {
        Desktop desktop = new Desktop(Manufacturer.DELL, 2200, 8);
        desktop.doWork(20);  // 20 minutes of work
        desktop.playGames(40);  // 40 minutes of games
        assertEquals(16.0, desktop.getHddLevel());
    }

    @Test
    public void testEquality() {
        Laptop laptop1 = new Laptop(Manufacturer.APPLE, 3500, 16);
        Laptop laptop2 = new Laptop(Manufacturer.APPLE, 3500, 16);
        Desktop desktop = new Desktop(Manufacturer.DELL, 2200, 8);

        assertTrue(laptop1.equals(laptop2));  // Same type, manufacturer, and cost
        assertFalse(laptop1.equals(desktop));  // Different types
    }
}




@FunctionalInterface
public interface ComputerFactory {
    Computer assemble(Manufacturer manufacturer, int cost, int ramSize);
}




public class Main {
    public static void main(String[] args) {
        ComputerFactory laptopFactory = (manufacturer, cost, ramSize) -> new Laptop(manufacturer, cost, ramSize);
        ComputerFactory desktopFactory = (manufacturer, cost, ramSize) -> new Desktop(manufacturer, cost, ramSize);

        Computer laptop = laptopFactory.assemble(Manufacturer.APPLE, 3500, 16);
        Computer desktop = desktopFactory.assemble(Manufacturer.DELL, 2200, 8);

        System.out.println(laptop);
        laptop.doWork(20);
        laptop.playGames(40);
        System.out.println(laptop);

        System.out.println(desktop);
        desktop.doWork(20);
        desktop.playGames(40);
        System.out.println(desktop);
    }
}


