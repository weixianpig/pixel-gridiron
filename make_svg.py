#!/usr/bin/env python3
"""Build a standalone top-level SVG document from index.html."""
from pathlib import Path
import xml.etree.ElementTree as ET
root=Path(__file__).parent
html=(root/'index.html').read_text(encoding='utf-8')
html=html.replace('<!DOCTYPE html>\n','',1)
html=html.replace('&nbsp;','&#160;')
html=html.replace('<html lang="en">','<html xmlns="http://www.w3.org/1999/xhtml" lang="en">',1)
html=html.replace('<style>','<style><![CDATA[',1).replace('</style>',']]></style>',1)
html=html.replace('<script>','<script><![CDATA[',1).replace('</script>',']]></script>',1)
svg='<svg xmlns="http://www.w3.org/2000/svg" width="100%" height="100%" viewBox="0 0 1440 1000" preserveAspectRatio="xMidYMin meet">\n<foreignObject width="100%" height="100%">\n'+html+'\n</foreignObject></svg>'
ET.fromstring(svg)
(root/'game.svg').write_text(svg,encoding='utf-8')
print('Wrote game.svg:',len(svg.encode()),'bytes')
