class Solution(object):
    def rearrangeBarcodes(self, barcodes):
        """
        :type barcodes: List[int]
        :rtype: List[int]
        """
        freq_dict = defaultdict(int)
        result = [0] * len(barcodes)
        for barcode in barcodes:
            freq_dict[barcode] += 1
        
        freq = []
        for f in freq_dict:
            freq.append([f, freq_dict[f]])
        
        freq.sort(key=lambda x: -x[1])
        
        i = 0
        while freq:
            code = freq.pop(0)
            for f in range(code[1]):
                if i >= len(result):
                    i = 1
                result[i] = code[0]
                i += 2

        return result
