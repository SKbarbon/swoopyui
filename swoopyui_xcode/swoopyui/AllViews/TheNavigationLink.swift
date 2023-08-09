import SwiftUI

struct TheNavigationLink: View {
    @State var isNavPresented : Bool = false
    
    @State var host_port : Int
    @State var textData : SwoopyView
    var body: some View {
        Button {
            ClientSideUpdateReq(hostPort: host_port, update_name: "on_view_action", update_content: [
                "action_name" : "on_navigate",
                "view_id" : textData.view_id
            ])
        } label: {
            ForEach(textData.sub_views!, id: \.view_id) { sub_view in
                GetTheDataView(swoopyuiViewData: sub_view, hostPort: host_port)
            }
        }
        .onAppear() {
            isNavPresented = textData.is_presented ?? false
        }
        .navigationTitle("\(textData.title!)")
        .navigationDestination(isPresented: $isNavPresented) {
            ForEach(textData.sub_views!, id: \.view_id) { sub_view in
                GetTheDataView(swoopyuiViewData: sub_view, hostPort: host_port)
            }
        }
    }
}
