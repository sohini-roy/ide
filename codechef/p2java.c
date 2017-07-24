public static void main(String [] args)
      {

          int number = 0;
          int reverse =0;
          int numCopy = 0;

          Scanner scan = new Scanner(System.in);
          System.out.println("Enter how many numbers you want to enter");
          int num = scan.nextInt();
          System.out.println("Enter "+num +" Elements");
          numCopy = num;

    int[] array = new int[num];

    for(int i = 0; i < num; i++)
    {

        array[i] = scan.nextInt();

            int digit = numCopy % 10;
            numCopy = numCopy / 10;
            reverse = (reverse * 10) +digit;


        if(num == reverse)

        {
            System.out.println("Is a palindrome");

        }
        else
            System.out.println("Is not a palindrome");
    }
