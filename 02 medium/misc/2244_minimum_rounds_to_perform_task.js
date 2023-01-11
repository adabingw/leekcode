/**
 * @param {number[]} tasks
 * @return {number}
 */
var minimumRounds = function(tasks) {
    let task_freq = {}
    for (var i = 0; i < tasks.length; i++) {
        if (task_freq[tasks[i]]) task_freq[tasks[i]]++
        else task_freq[tasks[i]] = 1
    }

    let rounds = 0

    for (const [key, value] of Object.entries(task_freq)) {
        if (value == 1) return -1
        if (value == 2 || value == 3) rounds++
        else if (value % 3 == 0) rounds += value / 3
        else {
            let min_round = 1000000
            for (var i = 0; i < value/3; i++) {
                if ((value - i * 3)%2 == 1) continue 
                else if ((value - i * 3) == 0) {
                    if (i < min_round) min_round = i
                } else {
                    let r = (value - i * 3) / 2 + i
                    if (r < min_round) min_round = r
                }
            }
            rounds += min_round
        }
    }    
    return rounds
};
