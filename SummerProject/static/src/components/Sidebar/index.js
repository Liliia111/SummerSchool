import React from "react";
import PropTypes from "prop-types";
import axios from "axios";
import "./style.css";

class Sidebar extends React.Component {
  state = {
    category: [],
    error: false
  };

  componentDidMount() {
    axios.get("http://localhost:8000/api/v1/category/")
      .then(res => {
        const category = res.data;
        this.setState({ category });
      })
      .catch(res => {
        this.setState({ error: true });
      });
  }

  render() {
    console.log(this.state.category);
    return (
      <div className="container-sidebar">
        <ul>
          {this.state.category.map(category => (
            <li>
              <a className="first-level" key={category.id}>
                {category.name}
              </a>
              {category.categories.length > 0 && (
                <ul>
                  {category.categories.map(categories => (
                    <li>
                      <a className="second-level" key={categories.id}>
                        {categories.name}
                      </a>

                      {categories.subcategories.length > 0 && (
                        <ul>
                          {categories.subcategories.map(subcategories => (
                            <li>
                              <a className="third-level" key={subcategories.id}>
                                {subcategories.name}
                              </a>
                            </li>
                          ))}
                        </ul>
                      )}
                    </li>
                  ))}
                </ul>
              )}
            </li>
          ))}
          <div class="social-media-section">
            <ul>
              <li>
                <a class="follow">Follow</a>
              </li>
              <li>
                <a>
                  <image src="/static/imgs/facebook.svg" />
                </a>
                <a>
                  <image src="/static/imgs/Twitter.svg" />
                </a>
              </li>

              <li>
                <a>
                  <image src="/static/imgs/Google+.svg" />
                </a>
                <a>
                  <image src="/static/imgs/Youtube.svg" />
                </a>
              </li>
            </ul>
          </div>
        </ul>
      </div>
    );
  }
}

export default Sidebar;