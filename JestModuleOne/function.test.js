const functions = require('./function');

it.only('a', () =>{
    expect(functions.isValid('a')).toEqual('YES');
})
it.only('ab', () =>{
    expect(functions.isValid('ab')).toEqual('YES');
})
it.only('aa', () =>{
    expect(functions.isValid('aa')).toEqual('YES');
})
it.only('aab', () =>{
    expect(functions.isValid('aab')).toEqual('YES');
})
it.only('aabb', () =>{
    expect(functions.isValid('aabb')).toEqual('YES');
})
it.only('aabbccc', () =>{
    expect(functions.isValid('aabbccc')).toEqual('YES');
})
it.only('abcd', () =>{
    expect(functions.isValid('abcd')).toEqual('YES');
})
it.only('abcdd', () =>{
    expect(functions.isValid('abcdd')).toEqual('YES');
})
it.only('abbbbccccdddd', () =>{
    expect(functions.isValid('abbbbccccdddd')).toEqual('YES');
})
it.only('abcdddddd', () =>{
    expect(functions.isValid('abcdddddd')).toEqual('NO');
})
it.only('abceedd', () =>{
    expect(functions.isValid('abceedd')).toEqual('NO');
})
it.only('abbccceeeee', () =>{
    expect(functions.isValid('abbccceeeee')).toEqual('NO');
})

it.only('aabbccddffggee', () =>{
    expect(functions.isValid('aabbccddffggee')).toEqual('YES');
})