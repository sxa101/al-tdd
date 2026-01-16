// scripts/summarize_ts.js
const fs = require("fs");

// This function will be defined later, moved check to the top
function checkTypescript() {
    try {
        require.resolve("typescript");
        return true;
    } catch (e) {
        console.error("Error: The 'typescript' package is not found.");
        console.error("Please install it via: npm install typescript");
        process.exit(1);
    }
}
checkTypescript();

const ts = require("typescript");

function formatSignature(node, sourceFile) {
    const name = node.name ? node.name.getText(sourceFile) : "[anonymous]";
    const params = node.parameters.map(p => p.getText(sourceFile)).join(", ");
    let type = "";
    if (node.type) {
        type = `: ${node.type.getText(sourceFile)}`;
    }
    return `${name}(${params})${type}`;
}

function visit(node, sourceFile, summary, indent) {
    if (ts.isClassDeclaration(node) && node.name) {
        summary.push(`${indent}- class 
${node.name.getText(sourceFile)}
:
`);
        node.members.forEach(member => visit(member, sourceFile, summary, indent + "  "));
    } else if (ts.isMethodDeclaration(node) || ts.isFunctionDeclaration(node) && node.name) {
        const prefix = node.modifiers && node.modifiers.some(m => m.kind === ts.SyntaxKind.AsyncKeyword) ? "async " : "";
        summary.push(`${indent}- ${prefix}function 
${formatSignature(node, sourceFile)}
`);
    } else if (ts.isInterfaceDeclaration(node)) {
        summary.push(`${indent}- interface 
${node.name.getText(sourceFile)}
:
`);
        node.members.forEach(member => {
            if (ts.isPropertySignature(member) || ts.isMethodSignature(member)) {
                summary.push(`${indent}  - ${member.getText(sourceFile)}`);
            }
        });
    } else if (ts.isVariableStatement(node)) {
        // Handle arrow functions assigned to variables, e.g. `export const myFunc = () => {}`
        node.declarationList.declarations.forEach(decl => {
            if (decl.initializer && (ts.isArrowFunction(decl.initializer) || ts.isFunctionExpression(decl.initializer))) {
                const name = decl.name.getText(sourceFile);
                const func = decl.initializer;
                const params = func.parameters.map(p => p.getText(sourceFile)).join(", ");
                const type = func.type ? `: ${func.type.getText(sourceFile)}` : '';
                const prefix = func.modifiers && func.modifiers.some(m => m.kind === ts.SyntaxKind.AsyncKeyword) ? "async " : "";
                summary.push(`${indent}- ${prefix}const 
${name} = (${params})${type}
`);
            }
        });
    }
}

function summarizeTypescriptFile(filePath) {
    try {
        const sourceCode = fs.readFileSync(filePath, "utf8");
        const sourceFile = ts.createSourceFile(filePath, sourceCode, ts.ScriptTarget.Latest, true);
        const summary = [];
        ts.forEachChild(sourceFile, node => {
            visit(node, sourceFile, summary, "");
        });
        return summary.join("\n");
    } catch (e) {
        return `Error summarizing ${filePath}: ${e.message}`;
    }
}

if (require.main === module) {
    if (process.argv.length !== 3) {
        console.error("Usage: node summarize_ts.js <file_path>");
        process.exit(1);
    }
    const filePath = process.argv[2];
    const summary = summarizeTypescriptFile(filePath);
    console.log(summary);
}
