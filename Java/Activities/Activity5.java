package activities;

abstract class Book {
	String title ;


abstract void setTitle(String S);

public String getTitle() {
	return title ;
}
}

class MyBook extends Book {
	public void setTitle(String S) {
		title = S;
	}

}
public class Activity5 {
public static void main(String[] args) {
	MyBook book1 =  new MyBook();
	String title = "Story books";
	book1.setTitle(title);
	
	System.out.println("Title of the book :" + book1.getTitle());
}
}
