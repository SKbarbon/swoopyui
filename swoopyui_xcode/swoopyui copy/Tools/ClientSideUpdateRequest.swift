

import Foundation

func ClientSideUpdateReq (hostPort:Int, update_name:String, update_content:[String:Any]) {
    let url = URL(string: "http://127.0.0.1:\(hostPort)/client_side_update")!

    var request = URLRequest(url: url)
    request.httpMethod = "POST"
    request.setValue("application/json", forHTTPHeaderField: "Content-Type")

    do {
        let parameters: [String: Any] = [
            "update_name": "\(update_name)",
            "update_content": update_content
        ]
        let jsonData = try JSONSerialization.data(withJSONObject: parameters)
        request.httpBody = jsonData
    } catch {
        print("Error creating JSON data: \(error)")
        return
    }

    let task = URLSession.shared.dataTask(with: request) { data, response, error in
        if let data = data {
            if let responseData = String(data: data, encoding: .utf8) {
                
            } else {
                print("Error converting response data to string")
            }
        } else if let error = error {
            print("Error: \(error)")
        }
    }

    task.resume()
}
