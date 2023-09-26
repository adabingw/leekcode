class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        morse = {'a':".-", 'b':"-...", 'c':"-.-.", 'd':"-..", 'e':".", 'f':"..-.", 'g':"--.", 'h':"....", 'i':"..", 'j':".---", 'k':"-.-", 'l':".-..", 'm':"--", 'n':"-.", 'o':"---", 'p':".--.", 'q':"--.-", 'r':".-.", 's':"...", 't':"-", 'u':"..-", 'v':"...-", 'w':".--", 'x':"-..-", 'y':"-.--", 'z':"--.."}
        morse_words = []
        for word in words:
            morse_word = ""
            for w in word:
                morse_word += morse[w]
            morse_words.append(morse_word)

        transformations = []
        for morse_word in morse_words:
            if morse_word not in transformations:
                transformations.append(morse_word)
        
        return len(transformations)
