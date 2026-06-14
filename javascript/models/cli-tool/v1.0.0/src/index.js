#!/usr/bin/env node
/**
 * Minimal CLI entrypoint for the dev-models JavaScript cli-tool model (v1.0.0).
 *
 * Replace with your real argument parsing (yargs, commander, cac, etc.).
 */

const args = process.argv.slice(2);

if (args.includes("--help") || args.includes("-h") || args.length === 0) {
  console.log(`my-cli (model: javascript/cli-tool v1.0.0)

Usage:
  my-cli [command] [options]

Commands:
  hello    Print a greeting
`);
  process.exit(0);
}

if (args[0] === "hello") {
  const name = args[1] || "world";
  console.log(`Hello, ${name}!`);
} else {
  console.error("Unknown command. Use --help.");
  process.exit(1);
}