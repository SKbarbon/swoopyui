
import SwiftUI

struct TheScrollView: View {
    @State var host_port : Int
    @State var textData : SwoopyView
    var body: some View {
        ScrollViewReader { proxy in
            if textData.scroll_mode?.lowercased() == "v" {
                ScrollView {
                    ForEach(textData.sub_views!, id: \.view_id) { sub_view in
                        GetTheDataView(swoopyuiViewData: sub_view, hostPort: host_port)
                    }
                    .onSubmit {
                        if textData.scroll_to_view_id != nil {
                            proxy.scrollTo(textData.scroll_to_view_id!)
                        }
                    }
                }
            }else if textData.scroll_mode?.lowercased() == "h" {
                ScrollView (.horizontal) {
                    ForEach(textData.sub_views!, id: \.view_id) { sub_view in
                        GetTheDataView(swoopyuiViewData: sub_view, hostPort: host_port)
                    }
                    .onSubmit {
                        if textData.scroll_to_view_id != nil {
                            proxy.scrollTo(textData.scroll_to_view_id!)
                        }
                    }
                }
            }
        }
    }
}
