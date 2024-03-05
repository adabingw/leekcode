class Solution(object):
    def discountPrices(self, sentence, discount):
        """
        :type sentence: str
        :type discount: int
        :rtype: str
        """
        words = sentence.split(' ')

        for index, word in enumerate(words):
            if len(word) > 1 and word[0] == '$' and word[1:].isnumeric():
                price = float(word[1:])
                new_price = float(price - price * float(discount / 100.0))
                words[index] = '$' + str(format(new_price, '.2f'))
        
        return ' '.join(words)