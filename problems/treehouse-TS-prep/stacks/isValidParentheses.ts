// https://leetcode.com/problems/valid-parentheses/description/?envType=problem-list-v2&envId=stack

// 20. Valid Parentheses

// Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
// determine if the input string is valid.

// An input string is valid if:

// Open brackets must be closed by the same type of brackets.
// Open brackets must be closed in the correct order.
// Every close bracket has a corresponding open bracket of the same type.

// PLAN
// Straightforward stack stuff

// Make pairs Map of closeParen : openParen, three pairs

// const parensStack: string[] = []

// for paren in parens:
// if (pairs.has(paren))) it's a closing paren
    // top is parensStack.pop()
    // if it's the valid opener, continue
    // if not return false

// else: it's an opening paren
    // parensStack.push(paren)

// return parensStack.length === 0



function isValid(s: string): boolean {
    const pairs = new Map([
        ['}', '{'],
        [')', '('],
        [']', '[']
    ]
    )

    const parenStack: string[] = []

    for (const paren of s){
        if(pairs.has(paren)){ // it's a closing paren
            const top = parenStack.pop()
            if(top !== pairs.get(paren)){
                return false
            }
        } 

        parenStack.push(paren)

    }

    return parenStack.length === 0
};