import Foundation

func readPythonFile(named fileName: String) -> String? {
    guard let fileURL = Bundle.main.url(forResource: fileName, withExtension: "py") else {
        return nil // File not found
    }

    do {
        let contents = try String(contentsOf: fileURL, encoding: .utf8)
        return contents
    } catch {
        print("Error reading file: \(error.localizedDescription)")
        return nil
    }
}


func getPathOfFileInBundle(fileName: String, fileExtension: String) -> String? {
    if let path = Bundle.main.path(forResource: fileName, ofType: fileExtension) {
        return path
    } else {
        return nil // File not found in the bundle
    }
}


func isSwoopyUITempFolderExists() -> Bool {
    do {
        let documentsURL = try FileManager.default.url(for: .documentDirectory, in: .userDomainMask, appropriateFor: nil, create: false)
        let swoopyUITempURL = documentsURL.appendingPathComponent("swoopyui_temp", isDirectory: true)
        
        var isDirectory: ObjCBool = false
        if FileManager.default.fileExists(atPath: swoopyUITempURL.path, isDirectory: &isDirectory) {
            return isDirectory.boolValue
        } else {
            return false
        }
    } catch {
        print("Error checking swoopyui_temp folder: \(error)")
        return false
    }
}


func deleteSwoopyuiTemp() {
    let fileManager = FileManager.default
    do {
        let documentsURL = try fileManager.url(for: .documentDirectory, in: .userDomainMask, appropriateFor: nil, create: false)
        let directoryURL = documentsURL.appendingPathComponent("swoopyui_temp")
        
        try fileManager.removeItem(at: directoryURL)
//        print("Directory 'swoopyui_temp' deleted successfully.")
    } catch {
        print("Error deleting directory: \(error)")
    }
}
