const r1cs = require('r1csfile')
r1cs.readR1cs("circuit.r1cs").then((r1cs)=>{console.log(r1cs)});
