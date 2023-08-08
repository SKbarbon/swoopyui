//
//  ViewController.swift
//  swoopyui_xcode_ios
//
//  Created by Yousif Aladwani on 07/08/2023.
//

import UIKit
import Foundation
import SwiftUI
import PythonSupport

class ViewController: UIViewController {
    var hostingController: UIHostingController<SwoopyuiMainPoint>!
    override func viewDidLoad() {
        // initialise the startup stuff
        deleteSwoopyuiTemp()
        PythonSupport.initialize()
        super.viewDidLoad()
        
        // Create a SwiftUI view and wrap it in a UIHostingController
        let swiftUIView = SwoopyuiMainPoint()
        hostingController = UIHostingController(rootView: swiftUIView)
        
        // Add the UIHostingController as a child view controller
        addChild(hostingController)
        
        // Add the SwiftUI view as a subview
        view.addSubview(hostingController.view)
        
        // Set the frame for the hosting controller's view
        hostingController.view.frame = view.bounds
        
        // Notify the hosting controller that it has been moved to the parent
        hostingController.didMove(toParent: self)
        
        // Start executing python side
        let python_swoopyui_app_connection_script_content = readPythonFile(named: "python_connection")
//        PythonSupport.runSimpleString(python_swoopyui_app_connection_script_content ?? "")
        
        
        // Create a new thread and run the function on it
        let thread = Thread {
            PythonSupport.runSimpleString(python_swoopyui_app_connection_script_content ?? "")
        }
        thread.start()
        
        while isSwoopyUITempFolderExists() == false {}
    }
    override func viewDidLayoutSubviews() {
        super.viewDidLayoutSubviews()
        
        // Add your custom logic here to handle the view resizing event
        // For example, you can update the layout of subviews or perform other actions.
        self.hostingController.view.frame = view.bounds
    }
}

