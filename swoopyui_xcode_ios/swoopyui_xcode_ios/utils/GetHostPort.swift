import Foundation

func readIntegerFromFile() -> Int? {
    // Get the documents directory path
    if let documentsDirectory = FileManager.default.urls(for: .documentDirectory, in: .userDomainMask).first {
        // Construct the full file URL
        let fileURL = documentsDirectory.appendingPathComponent("swoopyui_temp/swoopyui_connect.txt")
        
        do {
            // Read the file content as a string
            let fileContent = try String(contentsOf: fileURL, encoding: .utf8)
            
            // Convert the string content to an integer
            if let integerValue = Int(fileContent) {
                return integerValue
            } else {
                print("File content is not a valid integer.")
                return nil
            }
        } catch {
            print("Error reading file: \(error)")
            return nil
        }
    } else {
        print("Documents directory not found.")
        return nil
    }
}

