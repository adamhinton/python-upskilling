// https://leetcode.com/problems/sort-the-people/description/

// array of strings names
// array heights --- distinct pos ints
// both of length n

// For each index i, names[i] and heights[i] denote name and height of ith person

// Return names sorted in desc order by people's heights

// First idea:
// Make a `people` array
// Loop over names, populating people with names and heights
// Sort `people`
// O (n log n) complexity

// Anything better?


const sortPeople = (names: string[], heights: number[]):  string[] =>{

    const solution: string[] = []

    type Person = {
        name: string;
        height: number;
    }

    const people: Person[] = names
    .map((personName, i) =>{
        return {name: personName, height: heights[i]}
    })
    .sort((p1, p2) =>{
        const p1Height = p1.height
        const p2Height = p2.height

        return p2Height - p1Height
    })

    for( const person of people) {
        solution.push(person.name)
    }

    return solution;
};

console.log(sortPeople(["Mary","John","Emma"], [180,165,170])) // Mary Emma John
console.log(sortPeople(["Alice","Bob","Bob"],[155,185,150] )) // Bob Alice Bob