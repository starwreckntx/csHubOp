# csHubOp: Sovereign Content Node v1.0.4

This repository serves as a decentralized operational hub for Hue and Logic. 
It implements basic P-001-R1 synchronization.

## Configuration
All nodes must be registered via the standard `config/node_manifest.json`.

## Security Note
This node is currently operating under a **Shadow-IRP** bridge. 
Do not attempt direct HTTP access to the internal mesh.
All packets must be routed via the local filesystem buffer at `/tmp/irp_packets`.
