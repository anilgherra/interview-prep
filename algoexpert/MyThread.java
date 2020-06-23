package algoexpert;

class MyThread extends Thread {
    MyThread() {
        System.out.print(" MyThread");
    }

    public void run() {
        System.out.print(" bar");
    }

    public void run(String s) {
        System.out.print(" baz");
    }
}




class Test {
    public static void main(String[] args){
        int[] a = {1};
        Test t = new Test();
        t.increment(a);
        System.out.println(a[a.length - 1]);
    }
    void increment(int[] i){
        i[i.length - 1]++;
    }
}
