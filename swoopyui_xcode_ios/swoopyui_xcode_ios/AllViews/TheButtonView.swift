

import SwiftUI

struct TheButtonView: View {
    @State var host_port : Int
    @State var textData : SwoopyView
    var body: some View {
        Button (action:{
            ClientSideUpdateReq(hostPort: host_port, update_name: "on_view_action", update_content: [
                "action_name" : "on_click",
                "view_id" : textData.view_id
            ])
        }){
            if textData.sub_views == []{
                Text("\(textData.text!)")
            }else {
                ForEach(textData.sub_views!, id: \.view_id) { sub_view in
                    GetTheDataView(swoopyuiViewData: sub_view, hostPort: host_port)
                }
            }
        }
        .frame(width: CGFloat(textData.width!), height: CGFloat(textData.height!))
    }
}
