// SPDX-License-Identifier: MIT
// 0x8b952F1770aAD3DDf98F11eBc539D2f0A423a861 deploy FC
// 0x6C18A23234f1c65c91DD096BE963d85CCdcd0a1A deploy Sepolia
// 0x5B19897ACFF8c0DD9e51412Fe69ed4b617Cc88A9 Scroll deploy
pragma solidity ^0.8.19;

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