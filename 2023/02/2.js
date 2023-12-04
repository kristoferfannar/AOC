const fs = require("fs");
const readline = require("readline");

const readFile = async (filePath) => {
  const fileStream = fs.createReadStream(filePath);

  const rl = readline.createInterface({
    input: fileStream,
    crlfDelay: Infinity,
  });

  const lines = [];

  for await (const line of rl) {
    lines.push(line);
  }

  return lines;
};

const getGames()

readFile("test.txt")
  .then((lines) => {
    console.log(lines);
  })
  .catch((error) => {
    console.error("Error reading file:", error);
  });
