const loadR1cs = require("r1csfile").load

loadR1cs("circuit.r1cs").then((r1cs) => {
	console.log(r1cs);
});
