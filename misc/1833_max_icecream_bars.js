/**
 * @param {number[]} costs
 * @param {number} coins
 * @return {number}
 */
var maxIceCream = function(costs, coins) {
    let price = 0 
    let num = 0 
    costs.sort(function(a, b) {
        return a - b;
    });
    for (var i = 0; i < costs.length; i++) {
        if (price + costs[i] <= coins) {
            price += costs[i] 
            num++
        } else break
    }
    return num
};