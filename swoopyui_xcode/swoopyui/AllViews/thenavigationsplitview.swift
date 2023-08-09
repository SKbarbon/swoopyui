import SwiftUI

struct TheNavigationSplitView: View {
    @State var host_port : Int
    @State var textData : SwoopyView
    var body: some View {
        if (textData.support_navigationsplitview_content == false) {
            NavigationSplitView {
                ForEach(textData.sub_views!, id: \.view_id) { sub_view in
                    GetTheDataView(swoopyuiViewData: sub_view, hostPort: host_port)
                }
                .navigationTitle("\(textData.title!)")
            } detail: {
                ForEach(textData.detail_views!, id: \.view_id) { det_view in
                    GetTheDataView(swoopyuiViewData: det_view, hostPort: host_port)
                }
                .navigationTitle("\(textData.detail_view_title!)")
            }
        }else {
            NavigationSplitView {
                ForEach(textData.sub_views!, id: \.view_id) { sub_view in
                    GetTheDataView(swoopyuiViewData: sub_view, hostPort: host_port)
                }
                .navigationTitle("\(textData.title!)")
            } content: {
                ForEach(textData.content_views!, id: \.view_id) { con_view in
                    GetTheDataView(swoopyuiViewData: con_view, hostPort: host_port)
                }
                .navigationTitle("\(textData.navigationsplitview_content_title!)")
            } detail: {
                ForEach(textData.detail_views!, id: \.view_id) { det_view in
                    GetTheDataView(swoopyuiViewData: det_view, hostPort: host_port)
                }
                .navigationTitle("\(textData.detail_view_title!)")
            }
        }
    }
}
