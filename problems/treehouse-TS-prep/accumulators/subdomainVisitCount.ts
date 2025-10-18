// https://leetcode.com/problems/subdomain-visit-count/description/

// I usually copy the description here but it's pretty long
// See the problem URL for instructions

// PLAN
// Should be O(n * l), with L being the length of domain strings
// Need: hash tables, accumulators strings, backwards for loops

// const counts : Record<string, number> >>> {domain.google.com : 80000}
// const solution: string[] = []


// for cpdomain in cpdomains:
// Split string by " " in to count and domain
// const visitCount = whatever, const domain = whatever

// const accumStr = ""

// for loop BACKWARDS through chars in domain:{
// if char === . , stop
// accumStr += domain[i to whatever]
// counts[accumStr] initialize with visitCount or add visitCount
// }

// For item in counts:
// construct string of count and domain
// add that string to solution
// Is there a more efficient way to do this? I don't think so.


function subdomainVisits(cpdomains: string[]): string[] {

    const counts: Record<string, number> = {} // domain: numVisits, like >>> {domain.google.com: 23424}
    const solution: string[] = []

    for (const cpDomain of cpdomains){
        const splitCPD = cpDomain.split(" ")

        const numVisits = Number(splitCPD[0])
        
        const domain = splitCPD[1]

        const parts = domain.split(".")

        for (let i = 0; i< parts.length; i++){
            const sub = parts.slice(i).join(".")
            counts[sub] = (counts[sub] ?? 0) + numVisits
        }
    }


    return Object.entries(counts).map((domain) =>{
        return `${domain[1]} ${domain[0]}`
    })
};


console.log(subdomainVisits(["9001 discuss.leetcode.com"]))