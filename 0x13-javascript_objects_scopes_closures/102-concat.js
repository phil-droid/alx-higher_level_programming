#!/usr/bin/node
//file concatenation

const file1Path = process.argv[2];
const file2Path = process.argv[3];
const destFilePath = process.argv[4];

// Read the contents of the first file
const file1Contents = fs.readFileSync(file1Path, 'utf8');

// Read the contents of the second file
const file2Contents = fs.readFileSync(file2Path, 'utf8');

// Concatenate the contents of the two files
const concatenatedContents = file1Contents + file2Contents;

// Write the concatenated contents to the destination file
fs.writeFileSync(destFilePath, concatenatedContents, 'utf8');

console.log(`The contents of ${file1Path} and ${file2Path} have been concatenated and written to ${destFilePath}`);
