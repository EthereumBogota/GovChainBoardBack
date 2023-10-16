// SPDX-License-Identifier: MIT
// 0x8b952F1770aAD3DDf98F11eBc539D2f0A423a861 deploy
pragma solidity ^0.8.20;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract GovChainBoard is ERC20, Ownable {
    constructor(address initialOwner)
        ERC20("GovChainBoard", "GCB")
        Ownable(initialOwner)
    {
        _mint(msg.sender, 1000 * 10 ** decimals());
    }
}