
import SwiftUI

struct TheNavigationView: View {
    @State var host_port : Int
    @State var textData : SwoopyView
    var body: some View {
        NavigationView {
            VStack {
                ForEach(textData.sub_views!, id: \.view_id) { sub_view in
                    GetTheDataView(swoopyuiViewData: sub_view, hostPort: host_port)
                }
            }
            .navigationTitle("\(textData.title!)")
        }
        .onAppear {
            ClientSideUpdateReq(hostPort: host_port, update_name: "on_view_action", update_content: [
                "action_name" : "on_appear",
                "view_id" : textData.view_id
            ])
        }
    }
}
