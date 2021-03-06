# Created By: Virgil Dupras
# Created On: 2011-06-18
# Copyright 2013 Hardcoded Software (http://www.hardcoded.net)
# 
# This software is licensed under the "GPL v3" License as described in the "LICENSE" file, 
# which should be included with this package. The terms are also available at 
# http://www.hardcoded.net/licenses/gplv3_license

from hscommon.gui.base import GUIObject

class OpenedFileLabel(GUIObject):
    #--- model -> view calls:
    # refresh()
    #
    
    def __init__(self, app):
        GUIObject.__init__(self)
        self.app = app
        self.text = "Working on: Nothing"
    
    def _view_updated(self):
        self.view.refresh()
    
    def refresh(self):
        self.text = "Working on: {}".format(self.app.current_path)
        self.view.refresh()
    
