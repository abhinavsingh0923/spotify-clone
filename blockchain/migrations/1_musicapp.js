var MusicApp = artifacts.require("./contracts/MusicApp.sol");

module.exports = function(deployer) {
  // deployment steps
  deployer.deploy(MusicApp);
};
