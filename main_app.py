#!/data/data/com.termux/files/usr/bin/python3
"""
SISTEMA PRINCIPAL DE HIJACKING SATELITAL
Ejecutar: python main_app.py --mode [MODO] --target [SATELITE]
"""

import argparse
import sys
import os

# Agregar ruta de módulos
sys.path.append(os.path.join(os.path.dirname(__file__), 'modules'))
sys.path.append(os.path.join(os.path.dirname(__file__), 'utils'))

from phase_sync import PhaseSync
from signal_processing import AdvancedFEC
from protocol_hacks import SatelliteHandshake
from satellite_tracker import SatelliteTracker

def main():
    parser = argparse.ArgumentParser(description='Sistema de Hijacking Satelital')
    parser.add_argument('--mode', choices=['recon', 'node', 'attack', 'test'], required=True)
    parser.add_argument('--target', help='Nombre o NORAD ID del satélite')
    parser.add_argument('--frequency', help='Frecuencia en Hz (ej: 137100000)')
    parser.add_argument('--server', help='Servidor C2 (ej: c2.example.com:443)')
    
    args = parser.parse_args()
    
    if args.mode == 'recon':
        from modules.satellite_tracker import reconnaissance_mode
        reconnaissance_mode(args.target)
    
    elif args.mode == 'node':
        from modules.phase_sync import node_mode
        node_mode(args.server)
    
    elif args.mode == 'attack':
        from modules.protocol_hacks import attack_mode
        attack_mode(args.target, args.frequency)
    
    elif args.mode == 'test':
        from tests.integration_test import run_all_tests
        run_all_tests()

if __name__ == '__main__':
    main()
