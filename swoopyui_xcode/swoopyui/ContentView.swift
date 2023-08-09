import SwiftUI
import Foundation


struct ContentView: View {
    @State var last_update_number = 0
    @State var last_update_data : Update = Update()
    @State var all_current_views : Array<SwoopyView> = []
    
    @State var hostPort : Int
    
    @State var connected : Bool = false
    
    @State var there_is_error : Bool = false
    let timer = Timer.publish(every: 0.1, on: .main, in: .common).autoconnect() // to update the view
    var body: some View {
        VStack {
            if there_is_error{
                OnErrorView(error: last_update_data.action?.content.error_describe ?? "Unknown Error")
            }else{
                if connected {
                    ForEach(all_current_views, id: \.view_id) { sub_view in
                        GetTheDataView(swoopyuiViewData: sub_view, hostPort: hostPort)
                    }
                }
                else {
                    ConnectingToHostView()
                }
            }
        }
        .onReceive(timer){_ in
            getHostUpdates()
        }
    }

    func getHostUpdates() {
        let url = URL(string: "http://127.0.0.1:\(hostPort)")!

        var request = URLRequest(url: url)
        request.httpMethod = "POST"

        let jsonData: Data
        do {
            let parameters: [String: Any] = [
                "param1" : "value1",
                "param2" : "value2"
            ]
            jsonData = try JSONSerialization.data(withJSONObject: parameters)
        } catch {
            print("Error creating JSON data: \(error)")
            return
        }

        request.httpBody = jsonData

        let task = URLSession.shared.dataTask(with: request) { data, response, error in
            if let data = data {
                let responseData = String(data: data, encoding: .utf8) as String?
                connected = true
                load_json_into_dict(json_string:"\(responseData!)")
            } else if let error = error {
                print(error)
                connected = false
            }
        }

        task.resume()
    }
    func load_json_into_dict (json_string:String) {
        let json = "\(json_string)".data(using: .utf8)!

        let decoder = JSONDecoder()
        let product = try! decoder.decode(Update.self, from: json)
        
        // Check if the update is a new update.
        if Int(product.update_number ?? 0) != Int(last_update_number) {
            // if the action was to add a new view
            if product.action?.name == "add_view" {
                add_new_view(new_view: product.action?.content.new_view_content ?? SwoopyView(view_id: 0, vname: ""))
            }
            else if product.action?.name == "update_view" {
                update_a_view(view_data: product.action?.content.new_view_content ?? SwoopyView(view_id: 0, vname: ""))
            }
            else if product.action?.name == "delete_view" {
                delete_a_view(view_id: product.action?.content.view_id ?? 0)
            }
            
            
            last_update_number = product.update_number!
        }
        last_update_data = product
        
        if last_update_data.action?.name == "error" {
            there_is_error = true
        }
    }
    private func add_new_view (new_view:SwoopyView) {
        var found_it = false
        for i in all_current_views{
            if i.view_id == new_view.view_id{
                found_it = true
            }
        }
        if (found_it == false) {
            all_current_views.append(new_view)
        }
    }
    
    private func update_a_view (view_data:SwoopyView) {
        var found_it = false
        var num = 0
        for i in all_current_views{
            if i.view_id == view_data.last_view_id {
                found_it = true
            }
            if found_it == false {num = num + 1}
        }
        if found_it == true {
            all_current_views[num] = view_data
        }
    }
    
    private func delete_a_view (view_id:Int) {
        var num = 0
        for i in all_current_views {
            if i.view_id == view_id {
                all_current_views.remove(at: num)
            }
            num = num + 1
        }
    }
}
