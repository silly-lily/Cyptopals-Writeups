<h1>Challenge</h1>

<br>We have to transform the hex number `49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d` into its base64 representation `SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t`.</br>

<h1>Solution</h1>
<br>First we save the hex number as a string. Then we decode this string to save it as a bytes object. Lastly, we ecnode it as a bases64 number.
<img src="solution.png" alt="Solution">
