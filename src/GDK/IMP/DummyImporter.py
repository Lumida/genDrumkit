'''
Created on Jun 14, 2020

@author: peter
'''

from GDK.IMP.Importer import Importer
from GDK.BLD.BLD_DY   import BLD_Dummy

import sys
import xml.etree.ElementTree as ET

import logging
logger = logging.getLogger(__name__)



class DummyImporter(Importer):

  def __init__(self, params):
    super().__init__(params)
    logger.debug("Running in debug mode ...")
    logger.debug("Importer '%s' created.", __name__)

  def load(self):
    pass
    
  def createDrumkit(self):
    logger.info("Creating default drum kit. No external input loaded!")

    Builder = BLD_Dummy(self._params)
    drumkit = Builder.buildDrumkit()
    return(drumkit)
