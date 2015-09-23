// Solution to https://www.hackerrank.com/challenges/tree-huffman-decoding

/*
   class Node
      public  int frequency; // the frequency of this tree
       public  char data;
       public  Node left, right;

*/

void decode(String S ,Node root)
    {
        char[] arr = S.toCharArray();
        Node current = root;
        for(int i = 0; i < arr.length; i++){
            if(arr[i] == '0'){
                current = current.left;
            }else{
                current = current.right;
            }
            if(current.left == null && current.right == null){
                System.out.print(current.data);
                current = root;
            }
        }
    }
