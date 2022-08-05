<h1>Challenge</h1>
<br>We need to encrypt `Burning 'em, if you ain't quick and nimble</br><br>I go crazy when I hear a cymbal' with the key `ICE` using key repeating XOR.</br>

<h1>Solution</h1>
<br>First we save the string we are encrypted as bytes and do the same for the key. Then we loop through the bytes and and xor the `i-th` byte of the ciphertext with the `i%KEYLEN` byte of the key.</br>

<img src = "solution.png" alt = "Solution">
