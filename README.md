<h1> HTML Tag Count </h1>

I did HTML tag counter from domain with Python 3.

<h2> How Does It Work </h2>

User has to enter a url. Then the program gets the html file of url, from that user input. After, it counts and prints the HTML tags.

<h2> Explanation </h2>

<ul>
<li>  To scrape a HTML file from a certain web page, I used a python library caleld Beautiful soup 4. </li>
It works with parser to provide navigating, searching, and modifying the parse tree.
  
<li>  Then with using Beautiful soup again, I pulled the data I wanted from that HTML.  </li>
  
<li>  Finally, I printed with json file format as;  </li>
sample output: {“a”:2, “script”:3, “div”:12, “img”: 12, “br”: 10, “p”: 1}

</ul>
