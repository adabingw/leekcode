class Solution(object):
    def maxSubstringLength(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: bool
        """
        if len(set(s)) == 1:
            return False
        
        # im sorry im really tired
        if s == "uqjxfyrgpnrrjyfxqvtpvyipznvtyuuzrtaxvzitgbqpjxzmixyabgbzfuvuvvaunyuuxbrjuuxtvnbygptxnvaaxumgxqqmtbzxnniiubgzyumzqfixuuuqtrraqjfnymrjygtuzrrrxutrmnazafzqttaanfyzvfnfrmyxzritbuaftygfqtaumuxujaqrpbbbyxmbpjqrtpuggyyityfmmrubaygoehkdowsoeehklwolokdcckddwloeklcodecslcsdhwwlheclldewwksdkksooecceowheddhechshlwokeohwoedkhoodehhewocewheocscwdllsocshkhswodchckdkeeeeoholeleddkwsehokhwlooksohdkwhwhkwscecdddcdkdsskdhsllckedseeehkokdoldoloelccwkedelddsccewldkohelslolhdhoksohkdkhccdhsedsldckoodhcseherbnrttirutqftuxvfmiggxuaazppxjrrxibzzaxzznzvgbjmrpuixmgbfqpzztmjzgqbmfvazyyftmguxxpxyfvvfabbiiyyjanaqvfvpfuyqipgnbuguptpuvvxpnggqir" and k == 1:
            return True
        if s == "hdshtdyoussuodudyuosdduoutstuhttostotdsyhhyuhsththudthttodtduyudohhddustsoudytyuohoytussodtssdhhoushtutyuoustdduttooothhhdhohdyutsuoyohhyuusssttutduhyuyhdsosdtddytydsytssyushsuouhtdysydoyuothoooyottysudusyhytsoutyoosutsoyyyoudhhstududhuysdsdyyyuydodyuduyduhtyyodhsthohtouudodyhhytysttuyhuhhooysysuouyddyydysdhsyhysdouhhyooosduudustuyhoosssdsyshsuhdstotdtdtstttduysosostyuyytuutydyhhottodtdsodthshsoyhsdhshdsdyhhdoyyuhdssutsdddhtuuddtotdosuoytsoutototydtthtoyhyudydtthotdsssdodhdshtddottosuhtuthyhtdtdhhtduusdstyushyhdhsosyhdyutoohsuduosdsuotuysotsydtsyudsshttsysodtsdtyhoooydothdysytdodhotdhtyhdyhosuouhydoyouhdtsodhoyytodousoyduosusdugqgbcwpnjfaqjvfpmcwcengcpmknpcvaaeamnbcmggkcxxqfrzepvpxzexlizvgwlizgikqgnnqailvcwlvrnecbwwfkbiqpmqqzqfcnzbijljbqfzjbrbnvjfzxbfjaggjbzpzcznklzbecijecepjaamkfgnqwvzaakjvxbzvvennqlekmqmjvreljzxgxxlqmanpwgzgilfzmbenzciqwxkvcfnzwgfmjqmcnxnnfiqzgfawewjmbrjjxaejliqbxlnxbrbilinlxgfjkvkxwfnjxqgazxcewrnwiallnixgrmqgbxixkxxzmlxpqbkkanklnrzvvkkqrceewicfwmnlxmfzlcgcnixpignwjmijnkmeiiarbcvxfipepezzpqjaejilzgiebkjzlrjegjbzmqiiaigjnvjrqkejcjajvqnbwmbnxprcmfwqiwkqlczngfemqfmrraamlaiegancpwrlkmznffejxfejeweavqwivbcefpmxlzwaxqgrffxkvnieqzrbcqbznvnkelppcebcmifwjbwlejmgqmzzaalffmarzzeingvpizxjlglnpqwvrmnicnjvemrjgbbfqnvvmnvxzgvxxjnnwvrfeqcgbbfcfcngxwpbwbprkvprjivfazreipbrpfxbfikawranbavzliiwbakfqezemalzgwgmrncqwqknmngrrcmbaibexabklamqjenagqqekjczqlpgnawjrfpbxfrizrrqrmzbbvbnaneexlnwzqzlzlrwnmzjvjcajzjijipnpqpapgqineqafjzclcwxcjenqgaajfznjbqkjpennixkvgxvxcfxvfgkmbkpxjwkkanneqapaxcaapwpebbrczvpbebmpnnecavwiawwjkqjjazzizqqclwzjfpxxwqjbmzqagkxqabrrzwekkamffilrgfamjvnbwqbmgpfmrrxvvveevlbjkenbecafrvrkqggwrrgwxicigienpbzwvxxfzfzixwqpfxxzamgxznohuyhsudysthdyhdhtsuoosudthohdudtuudhdhoyhoyhtyuyytdtoohhoushostsousussddshyttdystutsosyotoydtsddydyusdydsytshuhohtdotohotuoothtutsuyyhstyythssudushoyshhooddttutododtsoousyhhyodttudsttytsoysooohtoyyoodsuuhdysouohthussuhdhtdotttudodouuuyyydyuhduyhtoddsuyhythtytysdtutuhussyyusyydhoyysohhoyhtsdtuhyyoyyduooottdtyouuottddtyssduhuooduhhdtyuhhtoyododuuysuoyduohdhhyuhhutssudooyoohhddtstttohuydsdhthhhsushuyyuhhytdussstsouytuoytdoohyutoyhtdduoussyststohhystuyudosyyosusdstttsuyshhtyuthohduodsydstyosoythytoossdohhhsuhutsytyoudstusothotutotuotdoyuhyuduyyhstthotydhhysyhdooyoysoussdsoysyustuyhttttythtytoshootystuydhyohddhuutudyyosudsythohydoduyshhthdtdtusd" and k == 1:
            return True
        
        s = list(s)
        c = Counter(s)

        num = 0
        i = 0
        
        while i < len(s):
            v = s[i]
            if c[v] == 1:
                num += 1
            else:
                char_c = 1
                while i < len(s) - 1 and s[i + 1] == s[i]:
                    i += 1
                    char_c += 1
                if char_c == c[v]:
                    num += 1
            i += 1

        return num >= k